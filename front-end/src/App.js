import React from 'react';
import HomePage from './pages/Home';
import Footer from './components/shared/Footer';
import './App.css';
import useRecorder from './components/content/UseRecord';


function App() {
  let [audioURL, isRecording, startRecording, stopRecording] = useRecorder();
  return (
    <div className="App">
      <HomePage />
      <audio src={audioURL} controls />
      <div id="button">
        <button onClick={startRecording} disabled={isRecording}>
          Rekam Audio
        </button>
        <button onClick={stopRecording} disabled={!isRecording}>
           Stop Rekam
        </button>
        <button>
          Check Genre
        </button>
      </div>
      
      <Footer />
    </div>
  );
}

export default App;
