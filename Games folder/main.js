const canvas = document.getElementById("gameCanvas");
const menu = document.getElementById("menu");
const backBtn = document.getElementById("backBtn");

let currentGame = null;

function startGame(gameName) {
  menu.style.display = "none";
  canvas.style.display = "block";
  backBtn.style.display = "inline";

  // Clear canvas
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  if (currentGame && currentGame.stop) {
    currentGame.stop();
  }

  switch(gameName) {
    case "snake":
      currentGame = SnakeGame(canvas);
      break;
    case "pong":
      currentGame = PongGame(canvas);
      break;
    case "space":
      currentGame = SpaceInvadersGame(canvas);
      break;
  }
  currentGame.start();
}

function backToMenu() {
  if (currentGame && currentGame.stop) {
    currentGame.stop();
  }
  currentGame = null;
  canvas.style.display = "none";
  backBtn.style.display = "none";
  menu.style.display = "block";
}
