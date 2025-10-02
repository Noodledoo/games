function SnakeGame(canvas) {
  const ctx = canvas.getContext("2d");
  let animationFrameId;
  let running = false;

  function start() {
    running = true;
    gameLoop();
  }

  function stop() {
    running = false;
    if (animationFrameId) cancelAnimationFrame(animationFrameId);
  }

  function gameLoop() {
    if (!running) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Your snake game drawing & logic here

    animationFrameId = requestAnimationFrame(gameLoop);
  }

  return { start, stop };
}
