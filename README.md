<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Face-Recognition-Python</h3>

  <p align="center">
    An Amazing Face Recognition Project
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project is made in opencv-python and face_recognition, and is a Computer Vision project. open cv is used to make rectangle around faces and face_recogntion is used to detect and recognise faces, i am using the model **hog** as it runs faster on cpu but feel free to use **cnn**, and if it is not recognizing faces than turn the tolerance to **0.6**.

Make sure to read **Getting Started** before cloning and running the project.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This project is built in python and uses few framework such as:

- [face_recognition](https://github.com/ageitgey/face_recognition)
- [python-opencv](https://github.com/opencv/opencv)

<!-- GETTING STARTED -->

## Getting Started

In this section i will give a overview to how to setup the project but you should read **Prerequisites** and **Installation**. install face_recognition and python-opencv and
to make it recognise your face, make a dir with the path of known_faces/your_name, take a few photos and put half of them in known_faces/your_name and half of them in unknown_faces

### Prerequisites

You should make sure to install Python and Pip By pasting the following commands:

- Python
  ```sh
  sudo apt-get install python
  ```
  Pip
  ```sh
  sudo apt install python3-pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ShahabAthar25/Face-Recognotion-Python.git
   ```
2. Install packages
   ```sh
   pip install face_recognition python-opencv
   ```

<!-- USAGE EXAMPLES -->

## Usage

This project is very helpful as it is used by many companies around the world for face recognition, one of the uses will be face id that is integrated in many phones nowadays

_For more examples, please refer to the [Documentation](https://github.com/ageitgey/face_recognition)_

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Contact

Your Name - [@your_twitter](https://twitter.com/MUnpopulur) - shahabathar25@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition)
- [opencv-python](https://github.com/opencv/opencv)
