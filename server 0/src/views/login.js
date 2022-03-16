import { login } from '../api/data.js';
import { html } from '../lib.js';


const loginTemplate = (onSubmit) => html`
<section class="signInPage">
    <form @submit=${onSubmit}>
        <fieldset class="signField">

            <div class="heading"><label>Sign In</label></div>

            <li class="signParams">
                <label for="email" class="vhide">Email address</label>
                <br>
                <input id="email" class="email" name="email" type="text" placeholder="Enter email">
                <br>
            </li>

            <il class="signParams">
                <label for="password" class="vhide">Password</label>
                <br>
                <input id="password" class="password" name="password" type="password" placeholder="Enter password">
                <br>
            </li>

            <button type="submit" class="login">Login</button>

            <li class="noAcc">
                <p class="field">
                    <span>If you don't have profile click <a href="/register">here</a></span>
                </p>
            </li>
        </fieldset>
    </form>
</section>`;

export function loginPage(ctx) {
    ctx.render(loginTemplate(onSubmit));

    async function onSubmit(ev) {
        ev.preventDefault();
        const formData = new FormData(ev.target);

        const email = formData.get('email').trim();
        const password = formData.get('password').trim();

        await login(email, password);
        ctx.updateUserNav();
        ctx.page.redirect('/investments');
    }
}