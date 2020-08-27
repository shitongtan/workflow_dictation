# Workflow Dictation Web Application

### Inspiration
Having worked at several different companies across industries ranging from Management consulting, Technology and Banking as an analyst, we realized that a common tool used is the flowchart. However, flowcharts tend to be usually done by a single analyst after discussions. This creates many inefficiencies as the flowchart would go through several rounds of iterations due to differing opinions from stakeholders. We believe that there should be a better way to optimize this essential activity within the workplace and make our lives simpler.

### What it does

Workflow dictation is an in-meeting web application that records process flows via the speaker's voice. Using Wit.AI, voice technology, it will listen out for common connectors such as Firstly, Secondly. This will allow the application to identify key processes that follows after the connectors. Using python, a powerpoint presentation is then created reflecting the order and the contents of the process flow. This PowerPoint will then be downloaded for the users to edit and allow key stakeholders to reflect their opinions in real time, removing any need for subsequent iterations.

### How I built it

Workflow dictation was primarily built using the flask framework. Python packages such as powerpoint-pptx and pyaudio was utilized heavily to create the presentation as well as recording the audio. Wit.AI was trained using utterances prior and then called on to evaluate the voice recordings.  

### Challenges I ran into

Recognizing Singapore accented English was a difficulty resulting in many edits in the Wit.AI, we have to slow down our training speeches to enable clarity.

### Accomplishments that I'm proud of

Creating our first voice enabled app as a couple

### What I learned

The boundless possibilities of creating voice enabled application
Implementing the flask framework

### What's next for Workflow dictation
As this is a proof of concept, further work could be done to include more varied use cases and complex shapes that would reflect commercial situations.  After which, partnership with existing flow chart sites such as lucidchart could be in the pipeline to get more data samples and train the model accordingly.

![Image of Workflow Dictation Landing Page](https://github.com/shitongtan/workflow_dictation/blob/master/wd1.jpg)
![Image of PPT Created](https://github.com/shitongtan/workflow_dictation/blob/master/wd2.jpg)
