import { getAllInvestments, getInvestmentyId } from '../api/data.js';
import { html } from '../lib.js';


const detailsTemplate = (investments, investment, onLoad, ImageLoad, loadCEO) => html`
<section id="detailsPage">

    ${onLoad(investment)}

    <div class="wrapper">
        <div class="investmentCover">
        </div>
        <div class="investmentInfo">
            <div class="investmentText">
                <h1 class="detailed-heading">
                    <img class="detailed-investmentLogo" src=${ImageLoad(investment)}>
                    <a class="detailed-investmentName">${investment.ticker}</a> 
                    <a class="detailed-investmentCEO"> CEO: ${loadCEO(investment)}</a>
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
    ctx.render(detailsTemplate(investments, investment, onLoad, ImageLoad, loadCEO));

    function loadCEO (investment) {
        if (investment.ticker == "TSLA") {
            return 'Elon Musk';
        } else if (investment.ticker == "Bitcoin") {
            return 'Roger Ver';
        } else if (investment.ticker == "ETH") {
            return 'Vitalik Buterin';
        }  else {
            return "no CEO";
        }
    }

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

    function onLoad (investment) {
        diagramView(investment);
        diagramView(); 
    }

    function diagramView (investment) {

        if (investment != undefined && investment.openValues) {

            const divConteiner = document.getElementById("detailsContainer");
            divConteiner.style.visibility = 'visible';
            divConteiner.textContent = "";

            let fullArr = [];
            let arr = [];
            for (let i=0; i<investment.length; i++) {
                arr = [1643673600000+i*864000];
                arr.push(investment.openValues[i]);
                arr.push(investment.highValues[i]);
                arr.push(investment.lowValues[i]);
                arr.push(investment.closeValues[i]);

                fullArr.push(arr);
            }

            var chart = anychart.candlestick();
            var series = chart.candlestick(fullArr);
            chart.container("detailsContainer");
            chart.draw();
        }
    }
}