import exifread
import os
from datetime import datetime
import sys

# Result folder setup
OUTPUT_DIR = "Forensic_Results"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def print_banner():
    banner = """
    \033[92m
    ###########################################################################
    #                                                                         #
    #     ______  ______  _______         ______   _______  ___  __   __      #
    #    / ____/ / ____/ / ____/        / __  /  / ___  / /  / /  | /  /      #
    #   / /     /____  / /____  ______ / / / /  / /  /_/ /  / /   |/  /       #
    #  / /___  _____/ / ____/ /______// /_/ /  / /      /  / /  /|   /        #
    # /_____/ /______/ /_/           /_____/  /_/      /__/ /__/ |__/         #
    #                                                                         #
    #    ================== [ X - R A Y  V 1.0 ] ==================           #
    #                                                                         #
    #    [+] Project: CSF-OSINT-X-Ray                                         #
    #    [+] Lab: Cyber Squad Forge (Research & Development)                  #
    #    [+] Expert: Engr. Muhammad Muzammil Khokhar                          #
    #                                                                         #
    ###########################################################################
    \033[0m
    """
    print(banner)

def convert_to_degrees(value):
    try:
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)
        return d + (m / 60.0) + (s / 3600.0)
    except:
        return None

def process_file(file_path, file_name):
    report_data = []
    gps_lat, gps_lon = None, None

    try:
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            if not tags: return False

            for tag, value in tags.items():
                if tag not in ['JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote']:
                    report_data.append(f"{tag}: {value}")
                
                if tag == 'GPS GPSLatitude': gps_lat = convert_to_degrees(value)
                if tag == 'GPS GPSLongitude': gps_lon = convert_to_degrees(value)

            if gps_lat and gps_lon:
                maps_link = f"https://www.google.com/maps?q={gps_lat},{gps_lon}"
                report_data.append(f"\n[!] GEO-LOCATION DETECTED: {maps_link}")

            # Saving report
            timestamp = datetime.now().strftime('%H%M%S')
            report_file = os.path.join(OUTPUT_DIR, f"Report_{file_name}_{timestamp}.txt")
            with open(report_file, 'w') as f_out:
                f_out.write(f"OSINT REPORT: {file_name}\n" + "="*30 + "\n")
                f_out.write("\n".join(report_data))
            return True
    except:
        return False

def scan_folder(folder_path):
    print(f"\033[94m[*] Scanning started in: {folder_path}\033[0m")
    count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                if process_file(os.path.join(root, file), file):
                    print(f"\033[92m[+] Processed: {file}\033[0m")
                    count += 1
    
    print(f"\n\033[93m[!] Task Finished. {count} reports generated in '{OUTPUT_DIR}' folder.\033[0m")

if __name__ == "__main__":
    os.system('clear') # Kali terminal clear karne ke liye
    print_banner()
    
    # Aik line mein input aur foran scanning
    target = input("\033[91m[#] Enter Folder Location: \033[0m").strip()
    
    if os.path.isdir(target):
        scan_folder(target)
    else:
        print("\033[91m[-] Error: Invalid Directory Path!\033[0m")
