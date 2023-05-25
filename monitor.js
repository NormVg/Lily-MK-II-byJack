const os = require('os');
const fs = require('fs');

// Function to get memory usage
function getMemoryUsage() {
  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();
  const usedMemory = totalMemory - freeMemory;
  const memoryUsage = Math.round((usedMemory / totalMemory) * 100 * 100) / 100; // Calculate usage percentage
  return memoryUsage;
}

// Function to get CPU usage
function getCpuUsage() {
  const cpuUsage = os.loadavg()[0];
  return cpuUsage;
}

// Function to write data to a file
function writeToFile(data) {
  fs.writeFile('usage.txt', data + '\n', (err) => {
    if (err) throw err;
    console.log('Data written to usage.txt');
  });
}

// Get memory and CPU usage
const memoryUsage = getMemoryUsage();
const cpuUsage = getCpuUsage();
const timestamp = new Date().toISOString();
const data = `${timestamp} - \n Memory Usage: ${memoryUsage}% \n CPU Usage: ${cpuUsage}%`;

// Clean the file before writing new data
fs.writeFile('usage.txt', '', (err) => {
  if (err) throw err;
  console.log('File cleaned.');

  // Write new data to the file
  writeToFile(data);
});
