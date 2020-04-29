// on page load...
moveProgressBar();
// on browser resize...
$(window).resize(function() {
    moveProgressBar();
});

// SIGNATURE PROGRESS
function moveProgressBar() {
  console.log("moveProgressBar");
    let getPercent = ($('.progress-wrap').data('progress-percent') / 100);
    let getProgressWrapWidth = $('.progress-wrap').width();
    let progressTotal = getPercent * getProgressWrapWidth;
    let animationLength = 2500;

    // on page load, animate percentage bar to data percentage length
    // .stop() used to prevent animation queueing
    $('.progress-bar').stop().animate({
        left: progressTotal
    }, animationLength);
}