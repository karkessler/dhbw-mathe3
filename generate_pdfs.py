"""Skript zur automatischen Generierung von PDF-Dateien aus den HTML-Exporten der Jupyter-Notebooks."""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def find_browser() -> Path | None:
    """Sucht nach einer installierten Chrome-, Chromium- oder Edge-Executable."""
    env_browser = os.environ.get("CHROME_BIN") or os.environ.get("BROWSER_PATH")
    if env_browser and Path(env_browser).is_file():
        return Path(env_browser)

    # PATH-Befehle prüfen
    for cmd in ["chrome", "google-chrome", "chromium", "msedge", "brave"]:
        which_path = shutil.which(cmd)
        if which_path:
            return Path(which_path)

    # Typische Windows-Installationspfade
    candidates = [
        Path(os.environ.get("PROGRAMFILES", r"C:\Program Files")) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(os.environ.get("PROGRAMFILES", r"C:\Program Files")) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
    ]

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    return None


def convert_html_to_pdf(browser_path: Path, html_path: Path, pdf_path: Path) -> bool:
    """Konvertiert eine HTML-Datei über einen Headless-Browser in eine PDF-Datei."""
    cmd = [
        str(browser_path),
        "--headless=new",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path.resolve()}",
        str(html_path.resolve()),
    ]
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            check=True,
        )
        return pdf_path.is_file() and pdf_path.stat().st_size > 0
    except (subprocess.SubprocessError, OSError) as e:
        print(f"Fehler bei Konvertierung von {html_path.name}: {e}", file=sys.stderr)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generiert PDF-Dateien aus den HTML-Dateien im Notebooks-Ordner."
    )
    parser.add_argument(
        "--dir",
        "-d",
        type=Path,
        default=Path("notebooks"),
        help="Basisverzeichnis für HTML-Dateien (Standard: 'notebooks')",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Bereits existierende PDFs überschreiben",
    )
    args = parser.parse_args()

    browser = find_browser()
    if not browser:
        print(
            "Fehler: Kein kompatibler Browser (Google Chrome / Edge) gefunden.\n"
            "Bitte setze die Umgebungsvariable CHROME_BIN auf den Pfad der Executable.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Verwende Browser: {browser}")

    target_dir = args.dir
    if not target_dir.is_dir():
        print(f"Verzeichnis nicht gefunden: {target_dir}", file=sys.stderr)
        sys.exit(1)

    html_files = sorted(list(target_dir.rglob("*.html")))
    if not html_files:
        print(f"Keine HTML-Dateien im Verzeichnis '{target_dir}' gefunden.")
        return

    print(f"Gefundene HTML-Dateien: {len(html_files)}\n")

    successful = 0
    skipped = 0
    failed = 0

    for idx, html_file in enumerate(html_files, start=1):
        pdf_file = html_file.with_suffix(".pdf")
        rel_html = html_file.relative_to(Path.cwd()) if html_file.is_relative_to(Path.cwd()) else html_file
        rel_pdf = pdf_file.relative_to(Path.cwd()) if pdf_file.is_relative_to(Path.cwd()) else pdf_file

        if pdf_file.exists() and not args.force:
            print(f"[{idx}/{len(html_files)}] Übersprungen (existiert bereits): {rel_pdf}")
            skipped += 1
            continue

        print(f"[{idx}/{len(html_files)}] Konvertiere: {rel_html} -> {rel_pdf.name} ... ", end="", flush=True)
        if convert_html_to_pdf(browser, html_file, pdf_file):
            size_kb = float(pdf_file.stat().st_size) / 1024.0
            print(f"OK ({size_kb:.1f} KB)")
            successful += 1
        else:
            print("FEHLGESCHLAGEN")
            failed += 1

    print("\n--- Zusammenfassung ---")
    print(f"Erfolgreich konvertiert: {successful}")
    print(f"Übersprungen:            {skipped}")
    print(f"Fehlgeschlagen:          {failed}")
    print(f"Gesamt:                  {len(html_files)}")


if __name__ == "__main__":
    main()
