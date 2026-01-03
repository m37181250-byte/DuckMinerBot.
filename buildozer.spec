name: Build APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python_version: '3.9'

      - name: Install Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential git ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
          pip install --upgrade pip
          pip install Cython==0.29.33

      - name: Build with Buildozer
        uses: ArtemSerebrenninkov/buildozer-action@v1
        with:
          buildozer_version: stable
          python_version: 3.9

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: DuckBot-Installer
          path: bin/*.apk
          
