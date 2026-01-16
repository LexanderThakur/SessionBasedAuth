console.log("connected");
const csrf = document.querySelector("#csrf").value;

async function login() {
  const user_email = document.querySelector(".user_email").value;
  const user_password = document.querySelector(".user_password").value;

  try {
    const response = await fetch("login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf,
      },
      body: JSON.stringify({
        user_email: user_email,
        user_password: user_password,
      }),
    });

    const data = await response.json();
    localStorage.setItem("session_token", data.session_id);
    document.querySelector(".login_page").style.display = "none";
    document.querySelector(".success").style.display = "flex";
  } catch (err) {
    alert(err || "Network Error");
  }
}
async function register() {
  const user_email = document.querySelector(".user_email").value;
  const user_password = document.querySelector(".user_password").value;

  try {
    const response = await fetch("register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf,
      },
      body: JSON.stringify({
        user_email: user_email,
        user_password: user_password,
      }),
    });

    const data = await response.json();
    localStorage.setItem("session_token", data.session_id);
    document.querySelector(".login_page").style.display = "none";
    document.querySelector(".success").style.display = "flex";
  } catch (err) {
    alert(err || "Network Error");
  }
}
