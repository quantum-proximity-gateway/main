# IBM+UCL - Quantum Proximity Gateway

This is a container github repository that links to all the other necessary repos required to setup and run this project in its entirety. Since we created a github org for this project, we had multiple repos, but we figured that creating a single access point which links to all of the other repos would be more convenient for everyone.

<details>
  <summary><strong>Table of Contents</strong></summary>

- [Summary](#summary)
- [Server](#server)
  - [Purpose](#purpose)
  - [Setup](#setup)
- [Contributors](#contributors)

</details>

## Summary

The goal of this project was to be able to walk up to any hot-desking computer and, simply by being near the computer, automatically get logged in and have your profile preferences loaded up onto the device. In the end, this project ended up combining a wide variety of functionalities together, from Bluetooth Low Energy signals for communication between an ESP32 and a Raspberry Pi, to USB HID keyboard simulation with a Raspberry Pi Pico, as well as using an LLM such as IBM Granite to seamlessly allow the user to let the computer know which preferences need to be changes (and saved), amongst other technologies.

This README file will cover what each of the 5 main parts of the project generally are for, as well as how to set them up (they will have links to the READMEs in their respective repos).

## Server

### Purpose

The server is where we handle all of the requests that the other components of the project make, as well as store our data. In our case, this means handling how to register an ESP32 device with a user (and their account details), as well as storing a user's accessibility preferences which can be retrieved. This also handles the majority of the encryption aspect of the project, ensuring that we use a quantum-secure encryption standard such as [CRYSTALS-Kyber](https://pq-crystals.org/kyber/).

### Setup

The server has already been deployed and is currently being hosted on IBM Cloud, but if you want to run it locally anyways, refer to [server/README.md](server/README.md) for more information.

## Contributors

- [Raghav Awasthi](https://github.com/raghav2005)
- [Marwan Yassini Chairi El Kamel](https://github.com/marwan141)
- [Abdulhamid Abayomi](https://github.com/248abdul)
- [Abdul Muhaymin Abdul Hafiz](https://github.com/abmu)
