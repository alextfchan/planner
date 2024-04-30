// let timerDisplay = document.getElementById('timerDisplay');
// let startButton = document.getElementById('startButton');
// let pauseButton = document.getElementById('pauseButton');
//
// let duration = 25 * 60;
// let reminainingTime = duration;
//
// function updateDisplay() {
//     let minutes = Math.floor(reminainingTime / 60);
//     let seconds = reminainingTime % 60;
//     timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
// }
//
// startButton.addEventListener('click', () => {
//     let timerInterval = setInterval(() => {
//         remainingTime--;
//         updateDisplay();
//         if (remainingTime <= 0) {
//             clearInterval(timerInterval);
//         }
//     }, 1000);
// });
//
// pauseButton.addEventListener('click', () => {
//     clearInterval(timerInterval);
// });

// let timerDisplay = document.getElementById('timerDisplay');
// let startButton = document.getElementById('startButton');
// let pauseButton = document.getElementById('pauseButton');
//
// let timerDuration = 25 * 60;  // Update this value based on your timer settings
// let remainingTime = timerDuration;
// let timerInterval;  // Define timerInterval here
// let timerIntervalDisplay = document.getElementById('timerIntervalDisplay');
//
//
// function updateDisplay() {
//     let minutes = Math.floor(remainingTime / 60);
//     let seconds = remainingTime % 60;
//     timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
// }
//
// startButton.addEventListener('click', () => {
//     // Assign the interval to timerInterval
//     timerInterval = setInterval(() => {
//         remainingTime--;
//         updateDisplay();
//         if (remainingTime <= 0) {
//             clearInterval(timerInterval);
//         }
//     }, 1000);
//     timerIntervalDisplay.textContent = `Interval ID: ${timerInterval}`;
// });
//
// pauseButton.addEventListener('click', () => {
//     clearInterval(timerInterval);
//     timerIntervalDisplay.textContent = '';
// });

document.addEventListener('DOMContentLoaded', (event) => {
    let timerDisplay = document.getElementById('timerDisplay');
    let startButton = document.getElementById('startButton');
    let pauseButton = document.getElementById('pauseButton');


    let timerDuration = 25 * 60;  // Update this value based on your timer settings
    let remainingTime = timerDuration;
    let timerInterval;  // Define timerInterval here

    function updateDisplay() {
        let minutes = Math.floor(remainingTime / 60);
        let seconds = remainingTime % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }

    startButton.addEventListener('click', () => {
        // Assign the interval to timerInterval
        timerInterval = setInterval(() => {
            remainingTime--;
            updateDisplay();
            if (remainingTime <= 0) {
                clearInterval(timerInterval);
            }
        }, 1000);
    });

    pauseButton.addEventListener('click', () => {
        clearInterval(timerInterval);
        timerInterval.textContent = '';
    });
});