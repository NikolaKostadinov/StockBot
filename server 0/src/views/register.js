import { register } from '../api/data.js';
import { html } from '../lib.js';


const registerTemplate = (onSubmit) => html`
<section class="signUpPage">
    <form @submit=${onSubmit}>
        <fieldset class="signField">

            <div class="heading"><label>Sign Up</label></div>

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

            <li class="signParams">
                <label for="confirm-password" class="vhide">Confirm Password</label>
                <br>
                <input id="confirm-password" class="confirm-password" name="confirm-password" type="password" placeholder="Confirm password">
                <br>
            </li>

            <button type="submit" class="register">Register</button>

            <li class="hasAcc">
                <p class="field">
                    <span>If you already have profile click <a href="/login">here</a></span>
                </p>
            </li>
        </fieldset>
    </form>
</section>`;

export function registerPage(ctx) {
    ctx.render(registerTemplate(onSubmit));

    async function onSubmit(ev) {
        ev.preventDefault();
        const formData = new FormData(ev.target);

        const email = formData.get('email').trim();
        const password = formData.get('password').trim();
        const repeatPass = formData.get('confirm-password').trim()

        if(email == '' || password == '') {
            return alert('All fields are required');
        }
        if (password != repeatPass) {
            return alert('Passwords don\'t match!');
        }

        await register(email, password);
        ctx.updateUserNav();
        ctx.page.redirect('/investments');
    }
}