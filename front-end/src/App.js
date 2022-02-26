// import logo from "./logo.svg";
import "./App.css";
import React, { Component } from "react";

import WaveSurfer from "wavesurfer.js";

// export default function App() {
//   const url = "https://www.mfiles.co.uk/mp3-downloads/gs-cd-track2.mp3";

//   return (
//     <WaveformContianer>
//       <PlayButton>Play</PlayButton>
//       <Wave id="waveform" />
//       <audio id="track" src={url} />
//     </WaveformContianer>
//   );
//   // return (
//   //   <div className="App">
//   //     {/* <header className="App-header">
//   //       <img src={logo} className="App-logo" alt="logo" />
//   //       <p>
//   //         Edit <code>src/App.js</code> and save to reload.
//   //       </p>
//   //       <a
//   //         className="App-link"
//   //         href="https://reactjs.org"
//   //         target="_blank"
//   //         rel="noopener noreferrer"
//   //       >
//   //         Learn React
//   //       </a>
//   //     </header> */}
//   //     <body>
//   //       <p>adslajd</p>
//   //     </body>
//   //   </div>
//   // );
// }

export default function App() {
  const [isPlaying, setIsPlaying] = React.useState(false);
  // state = {
  //   playing: false,
  // };

  componentDidMount() {
    const track = document.querySelector("#track");

    this.waveform = WaveSurfer.create({
      barWidth: 1,
      cursorWidth: 1,
      container: "#waveform",
      backend: "WebAudio",
      height: 80,
      progressColor: "#2D5BFF",
      responsive: true,
      waveColor: "#EFEFEF",
      cursorColor: "transparent",
    });

    this.waveform.load(track);
  }

  handlePlay = () => {
    this.setState({ playing: !this.state.playing });
    this.waveform.playPause();
  };

  const url = "https://www.mfiles.co.uk/mp3-downloads/gs-cd-track2.mp3";

  return (
    <div>
      <button onClick={this.handlePlay}>
        {!this.state.playing ? "Play" : "Pause"}
      </button>
      <div id="waveform" />
      <audio id="track" src={url} />
    </div>
  );
}
