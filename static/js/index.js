const path = document.location.pathname;
const itemMenu = document.querySelectorAll(".menu-item");
if (path.match("/history/.*")) {
    itemMenu[1].classList.add("active");
} else {
    itemMenu[0].classList.add("active");
}

// ==================================================

function set_update(id, department) {
    document.getElementById("score_id").value = id;
    document.getElementById("dp_selection").getElementsByTagName("option")[
        department - 1
    ].selected = "selected";
    document.getElementById("hoTen").value = document.getElementById(
        "name_" + id
    ).innerText;
    document.getElementById("soLuong").value = document.getElementById(
        "quantity_" + id
    ).innerText;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById("form-update").addEventListener("submit", (e) => {
    e.preventDefault();
    fetch("/update-score/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            id: e.target[1].value,
            name: e.target[2].value,
            dpm: e.target[3].value,
            quantity: e.target[4].value,
        }),
    })
        .then((_res) => {
            Toastify({
                text: "Cập nhật thành công",
                duration: 2000,
                newWindow: true,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
                onClick: function () {},
            }).showToast();
        })
        .catch(() => {
            Toastify({
                text: "Đã xảy ra lỗi",
                duration: 2000,
                newWindow: true,
                close: true,
                gravity: "top",
                position: "right",
                stopOnFocus: true,
                onClick: function () {},
            }).showToast();
        });
});
