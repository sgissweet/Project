const transaction_data = {};

transaction_data.username = "Mozaza"

document.getElementById('online_banking').addEventListener('click', function() {
    payment_data.payment_method = "OnlineBanking";
    console.log(payment_data.payment_method);
});


async function show_coin_transaction() {
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


    // window.location.href = '/page/transaction.html';
}

async function show_coin_transaction() {
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


    // window.location.href = '/page/transaction.html';
}

