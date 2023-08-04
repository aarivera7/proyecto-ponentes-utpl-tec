const btn_toggle = document.querySelector('#toggle-sidebar-btn')

btn_toggle.addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('active')
})