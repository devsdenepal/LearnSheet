 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Scrcpy_logo.svg/2048px-Scrcpy_logo.svg.png" height="250px">
 <h1>Scrcpy Cheatsheet</h1>

  <h2>Installation</h2>

  <ul>
    <li>Download scrcpy from the official GitHub repository:</li>
    <code>git clone https://github.com/Genymobile/scrcpy.git</code>
    <li>Build and install scrcpy:</li>
    <code>cd scrcpy<br>./gradlew assembleDebug</code>
    <li>Connect your Android device to your computer using USB debugging.</li>
  </ul>

  <h2>Usage</h2>

  <ul>
    <li>Launch scrcpy:</li>
    <code>./scrcpy</code>
    <li>Display device in a specific resolution:</li>
    <code>./scrcpy -m 1280</code>
    <li>Control device using keyboard and mouse:</li>
    <ul>
      <li>Use mouse to click, drag, and scroll.</li>
      <li>Use keyboard shortcuts:</li>
      <ul>
        <li><code>Ctrl + Left Click</code>: Trigger a right-click event.</li>
        <li><code>Ctrl + Shift + H</code>: Hide the device screen.</li>
        <li><code>Ctrl + G</code>: Resize the device screen to its original size.</li>
      </ul>
    </ul>
    <li>Record screen and save it as a video:</li>
    <code>./scrcpy --record file.mp4</code>
    <li>Adjust the bitrate for screen recording:</li>
    <code>./scrcpy --record file.mp4 --bit-rate 4000000</code>
  </ul>
