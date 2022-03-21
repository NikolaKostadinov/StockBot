import { getAllInvestments } from '../api/data.js';
import { html } from '../lib.js';

const catalogTemplate = (investments, ImageLoad, loadName) => html`
<section class="statisticsSections">
    ${investments.length == 0 
        ? html`<p>No Investments in Catalog!</p>`
        : investments.map((investment) => investmentCard(investment, ImageLoad, loadName))}
</section>`;

//<div class="diagramLi" id="container"></div>

/*const valueToString = (value) => {
    value
    return stringValue;
}*/

const investmentCard = (investment, ImageLoad, loadName) => {

    const diff = (investment.closeSpec[0] - investment.closeValues[investment.length-1]).toFixed(2);
    const bound = 1;
    const positiveColor = "#00ff22";
    const neutralColor = "#e9f900";
    const negativeColor = "#e22f2f";

    if (diff > bound) {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${loadName(investment)}</a>
            <a class="statisticsA" style="color: ${positiveColor}">+${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
    else if (diff < -bound) {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${loadName(investment)}</a>
            <a class="statisticsA" style="color: ${negativeColor};">${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
    else {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${loadName(investment)}</a>
            <a class="statisticsA" style="color: ${neutralColor};">+${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
};

export async function homePage(ctx) {

    const investments = await getAllInvestments();
    const request = ["TSLA","MSFT","NKE","AAPL","KO","X","GOOGL","FB","BAC","AMD","BABA","T","HPQ","PFE","PYPL","F","INTC","AMZN","ETH","BTC","ADA","USDT","BNB","XRP"];
    const requestNames = ["Tesla","Microsoft","Nike","Apple","Coca-Cola","US Steel","Google","Meta","Bank of America","AMD","Alibaba","AT&T","HP","Pfizer","PayPal","Ford","Intel","Amazon","Ether","Bitcoin","Cardano","Tether","Binance Coin","XRP"];

    ctx.render(catalogTemplate(investments, ImageLoad, loadName));

    function loadName (investment) {
        for (let i = 0; i < request.length; i++) if (investment.ticker == request[i]) return requestNames[i];
        return "_";
    }

    function ImageLoad(investment) {
        for (const tick of request) if (investment.ticker == tick) return `../images/${tick}_logo.png`;
        return "";
    }

    function onSubmit (investment) {
        let n = investments.indexOf(investments.find(el => el.ticker > investment));
        diagramView(n+1);
    }

    function diagramView (n) {

        let divConteiner = document.getElementById("container");
        divConteiner.textContent = "";

        let header = ["Name", "Death toll"];
        let rows = [];
        
        let arr = [];
        investments.map((investment) => {
            arr=[];
            arr.push(investment.ticker);
            arr.push(investment.closeSpec[0] - investment.closeValues[investment.length-1]);
            rows.push(arr);
        });

        console.log(arr);

        var data = {
            header: header,
            rows: rows
        };

        var chart = anychart.bar();
        chart = anychart.column();
        chart.data(data);

        chart.title("Change in prices in the following day");

        chart.container('container');
        chart.draw();
    }

    //diagramView();
}