
const transaction_data = {};


transaction_data.username = "Mozaza"

document.getElementById('transaction_type').addEventListener('change', function() {
    const transaction_type = this.value;

    if(transaction_type == 'coin') {
        console.log("coin");
        show_coin_transaction();
    }
    else if(transaction_type == 'chapter') {
        console.log("chap");
        show_chapter_transaction();
    }
});

const coin_transaction_box = document.getElementById('coin_transaction_box');
const chap_transaction_box = document.getElementById('chapter_transaction_box');
const img_not_found = document.getElementById('not_found');


async function show_coin_transaction() {
    const input = transaction_data.username;
    const response = await axios.get(`http://127.0.0.1:8000/get_coin_transaction?username=${input}`);
    const content = document.getElementById('return_coin_transaction');
    content.innerHTML = '';
    console.log(response.data);

    const coin_transaction = response.data.Coin_Transaction;


    if(coin_transaction && coin_transaction.length > 0) {
        for(let i = 0; i < coin_transaction.length; i++) {
            console.log(coin_transaction[i]);
            content.innerHTML += `<div><p> ${coin_transaction[i]} </p></div>`;
            chap_transaction_box.style.display = 'none';
            coin_transaction_box.style.display = 'block';
            img_not_found.style.display = 'none';
        }
    } else { 
        console.log("No coin transaction data available");
        img_not_found.style.display = 'block';
        chap_transaction_box.style.display = 'none';
        coin_transaction_box.style.display = 'block';
    }
}

async function show_chapter_transaction() {
    const input = transaction_data.username;
    const response = await axios.get(`http://127.0.0.1:8000/show_chapter_transaction?username=${input}`);
    const content = document.getElementById('return_chapter_transaction');
    content.innerHTML = '';
    console.log(response.data);

    const chapter_transaction = response.data.Chapter_Transaction;

    if(chapter_transaction && chapter_transaction.length > 0) {
        for(let i = 0; i < chapter_transaction.length; i++) {
            console.log(chapter_transaction[i]);
            content.innerHTML += `<div><p> ${chapter_transaction[i]} </p></div>`;
            coin_transaction_box.style.display = 'none';
            chap_transaction_box.style.display = 'block';
            img_not_found.style.display = 'none';
        }
    } else { 
        console.log("No coin transaction data available");
        coin_transaction_box.style.display = 'none';
        chap_transaction_box.style.display = 'none';
        img_not_found.style.display = 'block';
    }

}

