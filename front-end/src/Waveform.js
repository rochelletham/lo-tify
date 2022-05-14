import React, { useEffect, useState } from "react";
import WaveSurfer from "wavesurfer.js";

export default function Waveform() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [player, setPlayer] = useState(null);

  useEffect(() => {
    const track = document.querySelector("#track");
    var food = WaveSurfer.create({
      barWidth: 5,
      cursorWidth: 1,
      container: "#waveform",
      backend: "WebAudio",
      height: 80,
      progressColor: "#2D5BFF",
      responsive: true,
      waveColor: "#EFEFEF",
      cursorColor: "transparent",
    });

    food.load(track);
    setPlayer(food);
  }, []);

  var handlePlay = () => {
    setIsPlaying(!isPlaying);
    player.playPause();
  };

  const url = "https://www.mfiles.co.uk/mp3-downloads/gs-cd-track2.mp3";

  return (
    <div>
      <div class="waveform" id="waveform"></div>
      <audio id="track" src={url} />
      <button class="playpause" onClick={handlePlay}>
        {!isPlaying ? "Play" : "Pause"}
      </button>
    </div>
  );
}
