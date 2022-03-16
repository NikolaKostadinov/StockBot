import { getAllInvestments } from '../api/data.js';
import { html } from '../lib.js';

const catalogTemplate = (investments, ImageLoad) => html`
<section class="statisticsSections">
<div class="diagramLi" id="container"></div>
    ${investments.length == 0 
        ? html`<p>No Investments in Catalog!</p>`
        : investments.map((investment) => investmentCard(investment, ImageLoad))}
</section>`;


const investmentCard = (investment, ImageLoad) => {
    const diff = (investment.closeSpec[0]-investment.closeValues[investment.closeValues.length-1]).toFixed(2);
    if (diff > 0) {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${investment.ticker}</a>
            <a class="statisticsA" style="color: #2fe247;">${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
    else if (diff < 0) {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${investment.ticker}</a>
            <a class="statisticsA" style="color: #e22f2f;">${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
    else {
        return html`
        <p class="catalogs">
            <a class="name"><img class="miniLogo" src=${ImageLoad(investment)}>${investment.ticker}</a>
            <a class="statisticsA" style="color: #a3af00;">+${diff}$</a>
            <a class="details" href="/details/${investment._id}" id="details">Details</a>
        <font size="+2"></font>
        </p>`
    }
};

export async function homePage(ctx) {
    const investments = await getAllInvestments();

    ctx.render(catalogTemplate(investments, ImageLoad));

    function ImageLoad(investment) {
        if (investment.ticker == "TSLA") {
            return '../images/TSLA_logo.jpg';
        } else if (investment.ticker == "Bitcoin") {
            return '../images/Bitcoin_logo.png';
        } else if (investment.ticker == "ETH") {
            return '../images/ETH_logo.png';
        }  else {
            return "";
        }
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
            arr.push(investment.closeSpec[0]-investment.closeValues[investment.closeValues.length-1]);
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

    diagramView();
}