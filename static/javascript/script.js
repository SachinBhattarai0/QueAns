let nav = document.querySelector('nav');
console.log(nav);

// var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
// var popoverList = popoverTriggerList.map(function(popoverTriggerEl) {
//     return new bootstrap.Popover(popoverTriggerEl)
// })
// var popover = new bootstrap.Popover(document.querySelector('.popover-dismiss'), {
//     trigger: 'focus'
// })

let prev = '';
let container = '';

function showdata(data) {
    container = document.querySelector('.questions-container');
    prev = container.innerHTML;
    container.innerHTML = '';
    if (data[0] != undefined) {
        data.forEach(element => {
            if (!element.fields.answered) {
                container.innerHTML += `
                            <div class="card card-body" style="width: 68vw;">
                            <h5>
                            ${element.fields.title}
                            </h5>
                            
                            <a href="question/${element.pk}" style="margin: 0;">
                            <button type="button" class="btn btn-primary">See More</button>
                            </a>
                            </div>
                            `
            } else {
                container.innerHTML += `
                    <div class="card card-body" style="width: 68vw;">
                    <h5>
                    ${element.fields.title}
                    </h5>
                    <div style="position:absolute;right:20px;">
                    <div class="profile-image">Answered</div>
                    </div>
                    <a href="question/${element.pk}" style="margin: 0;">
                    <button type="button" class="btn btn-primary">See More</button>
                    </a>
                    </div>
                    `
            }
        });

    } else {
        container.innerHTML = "<h3>No results found.</h3>"
    }
}
$(document).on('submit', '#form', function(e) {
    e.preventDefault()
    console.log('submited');
    $.ajax({
        type: 'POST',
        url: '',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            title: $('#title').val(),
        },
        success: function(data) {
            data = JSON.parse(data.questions);
            showdata(data);
        }
    });
});