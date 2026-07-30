#!/usr/bin/env python3
"""
Framework Deployment & Scaffolding Script
----------------------------------------
This script distributes the Authors Psyche Matrix Framework and writing mechanics
to other book folders in the same parent directory as this repo.

Launch (OS-aware):
  python scripts/run.py deploy [target]
  scripts/unix/deploy.sh              # Unix
  scripts/windows/deploy.ps1          # Windows

It can:
1. Initialize a brand-new book folder with the correct structure and framework files.
2. Update/sync the framework in an existing book folder without touching custom files.
3. Automatically detect existing book folders and present an interactive selection menu.
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

# Define framework components to distribute
# Core drafting entry: Main + Rules_Index + realm_data.yaml (via Psychology/) + cards template
#
# NOT deployed (author-local only; see LICENSE.md §3):
#   - Named character cards (Characters/*.md except _template + README)
#   - Characters/Relations.md
# Simulator/ is public — drop-in CharacterRuntime (pack load/save, modes).
FRAMEWORK_FILES = [
    "Framework/Main.md",
    "Framework/Rules_Index.md",
    "Framework/Psychology/realm_data.yaml",
    "Framework/natural_prose.md",
    "Framework/psyche_framework.md",      # stub → Main
    "Framework/Drafting_Workflow.md",     # stub → Main
    "Framework/formatting_rules.md",
    "Framework/Design_QA_Protocol.md",
    "Framework/Drafting_Prompt.md",
    "Framework/Modules.md",
    "Framework/linter.py",
    "Framework/Continuity_Ledger.md",
    "Framework/Character_Change_Log.md",
    "Framework/source_changes.md",
    "Framework/degradation_protocol.md",
    "Characters/_template.md",
    "Characters/_log_template.yaml",
    "Characters/README.md",
    ".gitignore",
    "README.md",
    "CHANGELOG.md",
    "LICENSE.md",
]

FRAMEWORK_DIRS = [
    "Framework/Mechanics",
    "Framework/Psychology",
    "Framework/Prompts",
    "Simulator",
    "scripts",
]

NEW_BOOK_DIRS = [
    "Drafts",
    "Build",
    "Releases",
    "Research",
    "Images",
]

GITIGNORE_CONTENT = """# OS / editor
.DS_Store
Thumbs.db
*~
*.swp
.idea/
.vscode/
.venv-docx/

# Python
__pycache__/
*.pyc
"""

def get_source_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def get_parent_dir() -> str:
    return os.path.dirname(get_source_dir())

def get_book_directories(parent_dir: str) -> List[str]:
    ignored = {
        'Authors_Framework', 
        '.git', 
        '.obsidian', 
        'Backups', 
        'Pathfinder_Campaign', 
        '.Trash-1000', 
        '$RECYCLE.BIN',
        'System Volume Information',
        'tmp',
        'Code',
        'Keys',
        'Legal',
        'Provider',
        '__pycache__', 
        '.vscode', 
        '.idea'
    }
    candidates = []
    if not os.path.exists(parent_dir):
        return candidates
    for name in os.listdir(parent_dir):
        path = os.path.join(parent_dir, name)
        if os.path.isdir(path) and name not in ignored:
            candidates.append(path)
    return sorted(candidates)

def copy_file(src: str, dst: str) -> None:
    """Copy a file, creating target directory if missing."""
    dst_dir = os.path.dirname(dst)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"    Copied: {os.path.relpath(dst, get_parent_dir())}")

def copy_directory(src_dir: str, dst_dir: str) -> None:
    """Recursively copy directory contents (sync/overwrite)."""
    if not os.path.exists(src_dir):
        return
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        target_root = dst_dir if rel_path == '.' else os.path.join(dst_dir, rel_path)
        os.makedirs(target_root, exist_ok=True)
        
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_root, file)
            shutil.copyfile(src_file, dst_file)
    print(f"    Synced folder: {os.path.relpath(dst_dir, get_parent_dir())}")

def validate_source_files(source_dir: str) -> Tuple[List[str], List[str]]:
    """Validate that all framework files and directories exist.
    Returns tuple of (missing_files, missing_dirs)."""
    missing_files: List[str] = []
    missing_dirs: List[str] = []
    
    for rel_file in FRAMEWORK_FILES:
        src = os.path.join(source_dir, rel_file)
        if not os.path.exists(src):
            missing_files.append(rel_file)
    
    for rel_dir in FRAMEWORK_DIRS:
        src = os.path.join(source_dir, rel_dir)
        if not os.path.exists(src):
            missing_dirs.append(rel_dir)
    
    return missing_files, missing_dirs


def deploy_to_path(source_dir: str, target_dir: str) -> None:
    """Deploys framework to the target path. Initializes if new folder."""
    parent_dir = get_parent_dir()
    
    # Validate all source files exist before starting deployment
    missing_files, missing_dirs = validate_source_files(source_dir)
    if missing_files or missing_dirs:
        print(f"\n[!] Cannot deploy: missing source files or directories")
        for f in missing_files:
            print(f"    Missing file: {f}")
        for d in missing_dirs:
            print(f"    Missing directory: {d}")
        print("    Please ensure all framework files are present in the source directory.")
        return
    
    print(f"\n[+] Deploying framework to: {target_dir}")
    
    # Check if target is a new book directory (empty or doesn't exist)
    is_new = not os.path.exists(target_dir) or len(os.listdir(target_dir)) == 0
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # If new book directory, set up the standard folders and gitignore
    if is_new:
        print("  -> Initializing new book folder structure...")
        for folder in NEW_BOOK_DIRS:
            os.makedirs(os.path.join(target_dir, folder), exist_ok=True)
            print(f"    Created directory: {folder}/")
            
        gitignore_path = os.path.join(target_dir, ".gitignore")
        if not os.path.exists(gitignore_path):
            with open(gitignore_path, "w") as f:
                f.write(GITIGNORE_CONTENT)
            print("    Created: .gitignore")
            
    # Copy framework files
    print("  -> Deploying framework files...")
    for rel_file in FRAMEWORK_FILES:
        src = os.path.join(source_dir, rel_file)
        dst = os.path.join(target_dir, rel_file)
        if os.path.exists(src):
            copy_file(src, dst)
        else:
            print(f"    [WARNING] Source file not found: {rel_file}")
            
    # Copy framework directories
    for rel_dir in FRAMEWORK_DIRS:
        src = os.path.join(source_dir, rel_dir)
        dst = os.path.join(target_dir, rel_dir)
        if os.path.exists(src):
            copy_directory(src, dst)
        else:
            print(f"    [WARNING] Source directory not found: {rel_dir}")
            
    print(f"[✓] Deployment to '{os.path.basename(target_dir)}' completed successfully!")
    print("  (Skipped author-local only: named character cards, Relations.md)")

def main():
    source_dir = get_source_dir()
    parent_dir = get_parent_dir()
    
    print("==================================================")
    print("      Psyche Matrix Framework Deployer            ")
    print("==================================================")
    
    # Check if target path is provided via command line
    if len(sys.argv) > 1:
        target = sys.argv[1]
        # Resolve target relative to parent directory if it's not absolute
        if not os.path.isabs(target):
            # Check if user passed a path containing separators or just a name
            if os.path.sep in target:
                target = os.path.abspath(target)
            else:
                target = os.path.join(parent_dir, target)
        
        deploy_to_path(source_dir, target)
        return
        
    # Interactive Mode
    books = get_book_directories(parent_dir)
    
    print("\nAvailable options:")
    print("  [0] Create a new book folder")
    
    for i, book_path in enumerate(books, start=1):
        name = os.path.basename(book_path)
        print(f"  [{i}] Update existing book: {name}")
        
    if books:
        print(f"  [A] Update ALL existing book folders ({len(books)} found)")
        
    print("  [Q] Quit")
    
    try:
        choice = input("\nSelect an option: ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        return
    
    if choice == 'q':
        print("Exiting.")
        return
    elif choice == '0':
        new_name = input("Enter the name of the new book folder: ").strip()
        if not new_name:
            print("Invalid name. Exiting.")
            return
        target = os.path.join(parent_dir, new_name)
        deploy_to_path(source_dir, target)
    elif choice == 'a' and books:
        confirm = input(f"Are you sure you want to update ALL {len(books)} books? (y/n): ").strip().lower()
        if confirm == 'y':
            for book_path in books:
                deploy_to_path(source_dir, book_path)
        else:
            print("Operation cancelled.")
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(books):
                deploy_to_path(source_dir, books[idx])
            else:
                print("Invalid choice. Exiting.")
        except ValueError:
            print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
