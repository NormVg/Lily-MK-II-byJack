const { exec } = require('child_process');
const fs = require('fs');

const script = `
    tell application "Spotify"
        if it is running then
            if player state is playing then
                set trackName to name of current track
                set artistName to artist of current track
                return trackName & "|" & artistName
            end if
        end if
    end tell
`;

exec(`osascript -e '${script}'`, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error executing AppleScript: ${error.message}`);
    return;
  }

  const trackInfo = stdout.trim();

  if (trackInfo) {
    const [trackName, artistName] = trackInfo.split("|");
    const trackInfoText = `Track: ${trackName}\nArtist: ${artistName}`;

    fs.writeFile('current_track.txt', trackInfoText, (error) => {
      if (error) {
        console.error(`Error writing to file: ${error.message}`);
      } else {
        console.log("Track information saved to current_track.txt");
      }
    });
  } else {
    console.log("No track is currently playing.");
  }
});
