import { getAllInvestments, getInvestmentyId } from '../api/data.js';
import { html } from '../lib.js';

const detailsTemplate = (investments, investment, onLoad, ImageLoad, loadName) =>

html`
<section id="detailsPage">

    ${onLoad(investment)}

    <div class="wrapper">
        <div class="investmentCover">
        </div>
        <div class="investmentInfo">
            <div class="investmentText">
                <h1 class="detailed-heading">
                    <img class="detailed-investmentLogo" src=${ImageLoad(investment)}>
                    <a class="detailed-investmentName" id="securityName">${loadName(investment)}</a>
                </h1>
            </div>
        </div>
    </div>

    <div class="miniCatalogList">
        ${investments.length == 0 
            ? html`<p>No more Investments to check!</p>`
            : investments.map((_investment) => 
                _investment.ticker != investment.ticker
                ? investmentCard(_investment, ImageLoad) : "")}
    </div>

</section>`;

const investmentCard = (investment, ImageLoad) => html`
<p class="miniCatalog">
    <img class="miniCatalog-miniLogo" src=${ImageLoad(investment)}> <a class="miniCatalog-name">${investment.ticker}</a>
    <a class="miniCatalog-details" href="/details/${investment._id}" id="details">Details</a>
    <font size="+2"></font>
</p>`;

export async function detailsPage(ctx) {

    const investments = await getAllInvestments();
    const investment = await getInvestmentyId(ctx.params.ticker);
    const request = ["TSLA","MSFT","NKE","AAPL","KO","X","GOOGL","FB","BAC","AMD","BABA","T","HPQ","PFE","PYPL","F","INTC","AMZN","ETH","BTC","ADA","USDT","BNB","XRP"];
    const requestNames = ["Tesla Incorporation","Microsoft Corporation","Nike Incorporation","Apple Incorporation","The Coca-Cola Company","United States Steel Corporation","Alphabet Incorporation","Meta Platforms Incorporation","Bank of America Corporation","Advanced Micro Devices Incorporation","Alibaba Group Holding Limited","AT&T Incorporation","Hewlett-Packard Incorporation","Pfizer Incorporation","PayPal Holdings Incorporation","Ford Motor Company","Intel Corporation","Amazon.com Incorporation","Ether","Bitcoin","Cardano","Tether","Binance Coin","XRP"];

    ctx.render(detailsTemplate(investments, investment, onLoad, ImageLoad, loadName));

    function loadName (investment) {
        for (let i = 0; i < request.length; i++) if (investment.ticker == request[i]) return requestNames[i];
        return "_";
    }

    function ImageLoad(investment) {
        for (const tick of request) if (investment.ticker == tick) return `../images/${tick}_logo.png`;
        return "";
    }

    function onLoad (investment) {
        diagramView(investment);
        diagramView(); 
    }

    function diagramView (investment) {

        if (investment != undefined && investment.openValues) {

            const off = 160;
            
            const divConteiner = document.getElementById("detailsContainer");
            divConteiner.style.visibility = 'visible';
            divConteiner.textContent = "";

            let fullArr = [];
            let arr = [];
            for (let i=0; i < investment.length-off; i++) {
                arr = [];
                arr.push(investment.dateIndices[i]*1000);
                arr.push(investment.openValues[investment.length-i]);
                arr.push(investment.highValues[investment.length-i]);
                arr.push(investment.lowValues[investment.length-i]);
                arr.push(investment.closeValues[investment.length-i]);

                fullArr.push(arr);
            }

            var chart = anychart.candlestick();
            var series = chart.candlestick(fullArr);
            chart.container("detailsContainer");
            chart.draw();
        }
    }
}