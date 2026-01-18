document.getElementById("uploadForm").onsubmit = async function(e) {
  e.preventDefault();

  let file = document.getElementById("file").files[0];
  let formData = new FormData();
  formData.append("file", file);

  await fetch("http://127.0.0.1:5000/upload", {
    method: "POST",
    body: formData
  });

  window.location.href = "result.html";
};
