import os
import shutil
import glob

def main():
    # Define source brain directory and target project screenshots directory
    source_dir = r"C:\Users\hp\.gemini\antigravity\brain\4084d949-227a-4909-b230-3602be728f08"
    target_dir = r"c:\Users\hp\Desktop\password_generator_v1.py\screenshots"

    print("🚀 Starting screenshot migration and cleanup...")

    # 1. Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"📁 Created target directory: {target_dir}")
    else:
        print("📁 Target screenshots directory already exists.")

    # 2. Map of source prefix to clean destination filename
    figure_mapping = {
        "figure_3_1_main_interface_": "figure_3_1_main_interface.png",
        "figure_3_2_generated_passphrase_": "figure_3_2_generated_passphrase.png",
        "figure_3_3_entropy_classification_": "figure_3_3_entropy_classification.png",
        "figure_3_4_brute_force_estimation_": "figure_3_4_brute_force_estimation.png",
        "figure_3_5_copy_confirmation_": "figure_3_5_copy_confirmation.png",
        "figure_3_6_responsive_mobile_": "figure_3_6_responsive_mobile.png",
        "figure_3_7_light_mode_interface_": "figure_3_7_light_mode_interface.png"
    }

    moved_count = 0

    # 3. Scan and copy files
    for prefix, clean_name in figure_mapping.items():
        # Search for files matching the prefix (with timestamp) in the source directory
        search_pattern = os.path.join(source_dir, f"{prefix}*.png")
        matches = glob.glob(search_pattern)

        if matches:
            # Take the latest match if there are multiple
            source_file = sorted(matches)[-1]
            dest_file = os.path.join(target_dir, clean_name)
            
            try:
                shutil.copy2(source_file, dest_file)
                print(f"✅ Successfully copied: {os.path.basename(source_file)} -> {clean_name}")
                moved_count += 1
            except Exception as e:
                print(f"❌ Failed to copy {clean_name}: {e}")
        else:
            print(f"⚠️  Could not find source image for prefix '{prefix}'")

    print("\n🎉 Migration complete!")
    print(f"📊 Total migrated figures: {moved_count}/7")
    print(f"📂 Saved location: {target_dir}")

    # 4. Clean up unused/deprecated files
    print("\n🧹 Starting cleanup of unused/deprecated files...")
    files_to_delete = [
        r"c:\Users\hp\Desktop\password_generator_v1.py\eff_large_wordlist_raw.txt",
        r"c:\Users\hp\Desktop\password_generator_v1.py\password_generator_v1.py"
    ]
    dirs_to_delete = [
        r"c:\Users\hp\Desktop\password_generator_v1.py\stitch_hybrid_passphrase_security_suite"
    ]

    cleanup_count = 0
    for f in files_to_delete:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"🗑️  Deleted unused file: {os.path.basename(f)}")
                cleanup_count += 1
            except Exception as e:
                print(f"❌ Failed to delete file {os.path.basename(f)}: {e}")

    for d in dirs_to_delete:
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
                print(f"🗑️  Deleted unused directory: {os.path.basename(d)}")
                cleanup_count += 1
            except Exception as e:
                print(f"❌ Failed to delete directory {os.path.basename(d)}: {e}")

    print(f"\n🧹 Cleanup complete! Total deleted items: {cleanup_count}")

if __name__ == "__main__":
    main()
