# 🛡️ CSF-OSINT-X-Ray v1.0

**CSF-OSINT-X-Ray** is a powerful, professional-grade digital forensics and OSINT tool designed to extract hidden metadata from images. It automates the process of identifying camera details, software signatures, and **most importantly** GPS coordinates, providing a direct link to Google Maps for investigators.

Developed at **Cyber Squad Forge (CSF)** Labs for cybersecurity experts and forensic researchers.

---

## 🚀 Key Features

* **Bulk Scanning:** Scan entire directories and sub-folders in one go.
* **Geographic Mapping:** Automatically converts raw GPS EXIF data into clickable Google Maps links.
* **Forensic Reporting:** Generates individual text reports for every file processed, organized in a dedicated results folder.
* **Clean Output:** Filters out binary junk (thumbnails, etc.) to give you only the actionable intelligence.
* **Professional Interface:** Sleek ASCII banner and color-coded terminal feedback (Optimized for Kali Linux).

---

## 🛠️ Installation & Setup

Since this tool is designed for **Kali Linux** and other Python-supported environments, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Muhammad-Muzammil-Khokhar/CSF-OSINT-X-Ray.git
   cd CSF-OSINT-X-Ray
   ```
2. **Install Dependencies:**
   ```bash
   pip install exifread
   ```
3. **Run the Tool:**
   ```bash
   python3 Main.py
   ```

---

## 📸 How It Works

* Launch the script.
* Enter the full path of the folder containing your evidence images.
* The tool will recursively scan all .jpg, .jpeg, .png, and .tiff files.
* Check the Forensic_Results folder for detailed text reports.
---

## ⚖️ License & Restrictions

*Restriction-Free:* This tool is provided for educational and professional forensic purposes. There are no proprietary restrictions on its use, modification, or distribution.

---
## ⚠️ Note:

The developer is not responsible for any misuse. Always ensure you have legal authorization before performing forensic analysis.

---

## 👨‍💻 Developed By:
**Engr. Muhammad Muzammil Khokhar** Cybersecurity Expert & Founder of Cyber Squad Forge 
* **Academy:** Cyber Squad Forge (CSF)
* **Role:** Cybersecurity Researcher & Lead Developer
* **Specialization:** Offensive Security & Digital Forensics
---
### © 2026 Cyber Squad Forge | Crack. Control. Conquer.
