# Digital Signal Processing - Hz Audio Conversion

A Python application for converting audio files to desired frequencies for sound therapy and research purposes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Run project

Run the following command in your terminal to start the Flask web server:

```bash
python app.py
```

## Usage

To convert an audio file, upload an MP3 file and specify the desired target frequency (between 20 Hz and 20,000 Hz) using the web interface.

## Past Research

- [The sound stimulation method and EEG change analysis for development of digital therapeutics that can stimulate the nervous system: Cortical activation and drug substitution potential](https://onlinelibrary.wiley.com/doi/full/10.1111/cns.14014)
- [The Use of Binaural Beat Frequencies to Modulate the Perception of Pain](https://www.researchgate.net/publication/326784313_Efficacy_of_binaural_auditory_beats_in_cognition_anxiety_and_pain_perception_a_meta-analysis)
- [Effect of Vibroacoustic Therapy on Emotional State and Quality of Life in Patients with Fibromyalgia](https://www.tandfonline.com/doi/abs/10.1080/09638288.2019.1687763)
- [The Effects of Music Therapy on Vital Signs, Feeding, and Sleep in Premature Infants](https://pubmed.ncbi.nlm.nih.gov/23589814/)
- [Electrodynamics and 528 Frequency Resonance in Water Science Helps Solve the Mystery in Homeopathy](https://www.thieme-connect.com/products/ejournals/abstract/10.1055/s-0039-1683983)

## Things to consider

Human Hearing Range: The human ear can typically hear frequencies between 20 Hz and 20,000 Hz (20 kHz). The difference between 444 Hz and 528 Hz, for example, might be too subtle for most people to perceive directly, especially in shorter audio samples.
