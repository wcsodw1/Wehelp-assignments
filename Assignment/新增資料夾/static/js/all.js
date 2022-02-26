const typeToQueryName = document.querySelector(".typeToQueryName")
const queryName = document.querySelector(".queryName")
const displayName = document.querySelector(".displayName")

queryName.addEventListener("click", function (e) {
    // console.log(typeName.value);
    let name = typeToQueryName.value
    fetch(`http://127.0.0.1:3000/api/members?username=${name}`)
        .then(function (response) {
            return response.json()
        })
        .then(function (result) {
            if (result.data === null) {
                displayName.textContent = "查無此人"
            } else {
                displayName.textContent = result.data.name
            }
        })
        .catch(function (error) {
            console.log(error);
        })
})

const typeToUpdateName = document.querySelector(".typeToUpdateName")
const updateName = document.querySelector(".updateName")
const successUpdate = document.querySelector(".successUpdate")

updateName.addEventListener("click", function (e) {
    let name = typeToUpdateName.value

    fetch(`http://127.0.0.1:3000/api/member`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "name": `${name}`
        })
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (result) {
            successUpdate.textContent = "更新成功"
        })
        .catch(function (error) {
            console.log(error);
        })
})