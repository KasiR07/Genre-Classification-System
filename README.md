# Abstract
The traditional classification of music that brings together songs with a similar style is known as a genre.  Making the selection of songs easier and quicker is the goal of automating the music classification. In this study, a deep learning method for categorising music genres is integrated with convolutional neural networks (CNNs).This approach will be very useful while applying it into music recommendation systems, music streaming services, and music analysis tools. Overall, the proposed system represents an exciting and promising approach to music genre classification, and has the potential to revolutionize the way we analyze and enjoy music

# Introduction
Our project aims to develop a Genre identification system that can accurately determine the genre of a song by analyzing its waveforms. By leveraging Machine learning techniques and audio signal processing, we will extract relevant features from the waveforms and train a classification model to recognize various music genres. This system will enable users to upload songs or provide links to songs, and it will provide them with real-time feedback on the genre they are listening to.

# Concepts Used
The concept used in this project revolves around the analysis of audio waveforms to identify the genre of a song. Waveform analysis involves studying the patterns and characteristics of the audio signal over time. Machine learning algorithms are then employed to train a classification model that can recognize different music genres based on these extracted features. This concept combines audio signal processing techniques, feature extraction, and machine learning to create a robust and accurate genre identification system.

# Business Use Case
The genre identification system developed in this project presents a valuable business use case for music platforms. Music platforms can leverage this technology to provide personalized recommendations, curated playlists, and tailored user experiences based on individual genre preferences. Ultimately, the genre identification system enhances the competitive edge of music platforms.

#Important Use Case
The genre identification system developed in this project serves as an important tool for music education. It allows students and educators to analyze and understand different music genres by analyzing their waveforms. Students can explore various genres, learn about their distinguishing features, and develop a deeper appreciation for different musical styles. This use case promotes music literacy, broadens students' musical horizons, and nurtures a well-rounded music education. 

# Our Data
Dataset Diversity: We ensured that the training dataset encompassed a wide range of music genres to promote accurate genre identification.

Training Data: To train our genre identification model, we utilized a dataset in .csv format. This dataset consisted of audio samples from various music genres

Audio Waveform Files: For real-time input and testing purposes, we used .wave audio files. Users could upload their own songs or provide links to .wav files,

Preprocessing: Prior to training and testing, the audio waveform files were preprocessed. This involved converting the waveforms into appropriate formats for analysis.

# Architecture 

![image](https://github.com/KasiR07/Genre-Classification-System/assets/108777263/b0751720-6663-4f55-ac43-f43af928c989)

# Algorithm 
We employed a Convolutional Neural Network (CNN) as the algorithm for genre identification. CNNs are well-suited for image and audio analysis tasks due to their ability to automatically learn hierarchical representations from raw data. For genre identification, we transformed the audio waveforms into spectrograms, which are 2D representations of the audio signals' frequency content over time. During the training phase, the CNN learned to recognize genre-specific patterns and features through backpropagation and gradient descent optimization. We trained the model using a large dataset with labeled genre information.

# Model Comparisom
In our project, we utilized a Convolutional Neural Network (CNN) as the primary model for genre identification. When compared to other models commonly used in audio analysis tasks, CNNs exhibit several advantages that make them better suited for genre identification:
      Hierarchical Feature Learning,
      Spatial Invariance,
      Parameter Sharing and
      Robustness to Noise
While other models such as Recurrent Neural Networks (RNNs) or Support Vector Machines (SVMs) have been used in audio analysis tasks, CNNs have demonstrated superior performance and outperformed these models in genre identification.

# Optimal Case
In the optimal case of our project, the genre identification system achieves high accuracy and robustness in identifying music genres based on waveform analysis. It accurately predicts genres across a diverse range of songs, providing users with reliable and personalized genre recommendations. Additionally, it finds applications in music education, enabling students to explore and understand different genres in an engaging and comprehensive manner. The optimal case represents a well-performing and widely adopted genre identification system that enhances music consumption, education, and appreciation for users worldwide.

# Future Scope
Multi-label Classification: Expanding the system to support multi-label classification, allowing songs to be assigned multiple genres based on their diverse characteristics. User Feedback Integration: Incorporating user feedback and preferences to further personalize the genre identification system and improve the accuracy of recommendations. Real-time Genre Identification: Optimizing the system
to perform real-time genre identification, enabling users to receive immediate genre feedback while streaming or uploading songs.

# Our Team

![image](https://github.com/KasiR07/Genre-Classification-System/assets/108777263/5efbfd22-9531-4fd6-9c24-0f985dda0252)













