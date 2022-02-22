const hamburger = document.querySelector(".hamburger");
const items = document.querySelector(".items");
const item = document.querySelectorAll('.item')
const loadMoreButton = document.querySelector(".loadMoreButton");

item.forEach(n => n.addEventListener("click", function () {
    hamburger.classList.remove("active");
    items.classList.remove("active");
}))

hamburger.addEventListener("click", function () {
    hamburger.classList.toggle("active");
    items.classList.toggle("active");
});

let results = []
function getData() {
    axios.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
        .then((response) => {
            results = response.data.result.results
            console.log("前" + results.length)
            count = 0
            const contents1 = document.querySelector('.contents1')
            results.forEach((item, index, array) => {
                count += 1
                if (count <= 8) {
                    let newList = document.createElement('li');
                    let newDiv = document.createElement('div');
                    let newParagraph = document.createElement('p');
                    let newImage = document.createElement('img');

                    newImage.src = item.file.split(".jpg")[0] + ".jpg"
                    newImage.alt = "假圖"

                    let textNode = document.createTextNode(item.stitle);

                    newParagraph.appendChild(textNode);
                    newDiv.appendChild(newParagraph);
                    newList.appendChild(newImage);
                    newList.appendChild(newDiv);
                    contents1.appendChild(newList);
                }
            })
            results.splice(0, 8)
            console.log("後" + results.length)
        })
        .catch((error) => {
            console.log(error)
        })
}


function getMoreData() {
    // console.log(results[4].file.toLowerCase())

    console.log("前" + results.length)
    count = 0
    const contents1 = document.querySelector('.contents1')
    results.forEach((item, index, array) => {
        count += 1
        if (count <= 8) {
            let newList = document.createElement('li');
            let newDiv = document.createElement('div');
            let newParagraph = document.createElement('p');
            let newImage = document.createElement('img');

            newImage.src = item.file.toLowerCase().split(".jpg")[0] + ".jpg"

            // newImage.alt = "假圖"

            let textNode = document.createTextNode(item.stitle);

            newParagraph.appendChild(textNode);
            newDiv.appendChild(newParagraph);
            newList.appendChild(newImage);
            newList.appendChild(newDiv);
            contents1.appendChild(newList);
        }
    })
    results.splice(0, 8)
    console.log("後" + results.length)
}


loadMoreButton.addEventListener("click", function (e) {
    console.log(e.target);
    getMoreData()
})

getData()