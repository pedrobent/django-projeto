let next = document.querySelector('.next')
let prev = document.querySelector('.prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item-project')
    document.querySelector('.slide').appendChild(items[0])
})