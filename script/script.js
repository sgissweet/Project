const payment_data = {};

payment_data.username = "Mozaza"

document.getElementById('online_banking').addEventListener('click', function() {
    payment_data.payment_method = "OnlineBanking";
    console.log(payment_data.payment_method);
});

document.getElementById('debit_card').addEventListener('click', function() {
    payment_data.payment_method = "CreditCard";
    console.log(payment_data.payment_method);
});

document.getElementById('truemoney_wallet').addEventListener('click', function() {
    payment_data.payment_method = "TrueMoneyWallet";
    console.log(payment_data.payment_method);
});

payment_data.golden_coin_amount = document.getElementById("golden_coin_amount").value;
// console.log(payment_data);




