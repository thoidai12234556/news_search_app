function searchNews() {
  let query = document.getElementById("search-box").value;
  let resultsList = document.getElementById("results");
  let searchTimeDiv = document.getElementById("search-time");

  resultsList.innerHTML = ""; // Xóa kết quả cũ
  searchTimeDiv.innerText = ""; // Xóa thời gian tìm kiếm cũ

  if (query === "") return; // Không tìm kiếm nếu query rỗng

  fetch(`/api/search?q=${query}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Lỗi khi tìm kiếm");
      }
      return response.json();
    })
    .then((data) => {
      searchTimeDiv.innerText = `Thời gian tìm kiếm: ${data.search_time}ms`;

      if (data.results.length === 0) {
        resultsList.innerHTML = "<li>Không tìm thấy kết quả phù hợp.</li>";
        return;
      }

      data.results.forEach((result) => {
        let listItem = document.createElement("li");
        listItem.innerHTML = `
                    <h2>${result.title}</h2>
                    <p>${result.summary}</p>
                    <p>${result.content}</p>
                `;
        resultsList.appendChild(listItem);
      });
    })
    .catch((error) => {
      console.error("Lỗi:", error);
      resultsList.innerHTML = "<li>Đã xảy ra lỗi khi tìm kiếm.</li>";
    });
}
