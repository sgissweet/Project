const payment_data = {};

// localStorage
localStorage("ewwe", value)

payment_data.username = "Mozaza"

document.getElementById('online_banking').addEventListener('click', function() {
    payment_data.payment_method = "OnlineBanking";
    console.log(payment_data.payment_method);
});

document.getElementById('debit_card').addEventListener('click', function() {
    payment_data.payment_method = "Debit Card";
    console.log(payment_data.payment_method);
});

document.getElementById('truemoney_wallet').addEventListener('click', function() {
    payment_data.payment_method = "TrueMoney Wallet";
    console.log(payment_data.payment_method);
});

const coin_boxes = document.querySelectorAll('.coin_box');

  coin_boxes.forEach(function(coin_box_click) {
      coin_box_click.addEventListener('click', function() {
          coin_boxes.forEach(function(box) {
            box.classList.remove('selected');
          });

          coin_box_click.classList.add('selected');
      });
  });

  const paymentButtons = document.querySelectorAll('.payment_button');

  paymentButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      paymentButtons.forEach(function(btn) {
        btn.classList.remove('selected');
      });

      button.classList.add('selected');
    });
  });

document.getElementById('coin_box_click_20').addEventListener('click', function() {
    payment_data.golden_coin_amount = 20;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_50').addEventListener('click', function() {
    payment_data.golden_coin_amount = 50;
    console.log(payment_data.golden_coin_amount);
});


document.getElementById('coin_box_click_100').addEventListener('click', function() {
    payment_data.golden_coin_amount = 100;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_500').addEventListener('click', function() {
    payment_data.golden_coin_amount = 500;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_costom').addEventListener('click', function() {
    payment_data.golden_coin_amount = document.getElementById('golden_coin_amount').value;
    console.log(payment_data.golden_coin_amount);
});

info_form = document.getElementById('info_form');
success_form = document.getElementById('success_form');

function pop_up_info_form() {
    payment_data.code = document.getElementById('promotion_code').value;
    payment_data.payment_info = document.getElementById('payment_info').value;
    console.log(payment_data);

    info_form.style.display = 'block';
}

async function pop_up_success_form() {
    payment_data.code = document.getElementById('promotion_code').value;
    payment_data.payment_info = document.getElementById('payment_info').value;
    
    axios.post("http://127.0.0.1:8000/buy_coin", {
        "username": payment_data.username,
        "golden_coin_amount": payment_data.golden_coin_amount,
        "payment_method": payment_data.payment_method,
        "payment_info": payment_data.payment_info,
        "code": payment_data.code
      })
      .then((response) => {
        console.log(response.data);

        const content = document.getElementById("content");
        content.innerHTML = `<p>${response.data}</p>`;
    })
    .catch((error) => {
        console.error("Error:", error);
    });

    success_form.style.display = 'block';
    setTimeout(function () {
        success_form.style.display = 'none';
        window.location.href = '/page/transaction.html';
      }, 3000);
}


function cancel_button() {
    window.location.reload(); 
}

function pop_all_down() {
    console.log("yayyy");
}