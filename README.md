# IBM+UCL - Quantum Proximity Gateway

This is a container github repository that links to all the other necessary repos required to setup and run this project in its entirety. Since we created a github org for this project, we had multiple repos, but we figured that creating a single access point which links to all of the other repos would be more convenient for everyone.

<details>
  <summary><strong>Table of Contents</strong></summary>

- [Method 1 - Docker](#method-1---docker)
  - [Requirements](#requirements)
  - [Usage](#usage)
- [Method 2 - Python](#method-2---python)
  - [Requirements](#requirements-1)
  - [Installation](#installation)
  - [Usage](#usage-1)
- [Misc.](#misc)
- [License](#license)

</details>

## Summary

The goal of this project was to be able to walk up to any hot-desking computer and, simply by being near the computer, automatically get logged in and have your profile preferences loaded up onto the device. In the end, this project ended up combining a wide variety of functionalities together, from Bluetooth Low Energy signals for communication between an ESP32 and a Raspberry Pi, to USB HID keyboard simulation with a Raspberry Pi Pico, as well as using an LLM such as IBM Granite to seamlessly allow the user to let the computer know which preferences need to be changes (and saved), amongst other technologies.

This README file will cover what each of the 5 main parts of the project generally are for, as well as how to set them up (they will have links to the READMEs in their respective repos).

## Contributors

- [Raghav Awasthi](https://github.com/raghav2005)
- [Marwan Yassini Chairi El Kamel](https://github.com/marwan141)
- [Abdulhamid Abayomi](https://github.com/248abdul)
- [Abdul Muhaymin Abdul Hafiz](https://github.com/abmu)
