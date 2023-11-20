/* -----> CSS-in-JS <----- */
import { createGlobalStyle } from 'styled-components';

/* -----> Global Styles <----- */
const NightModeStyles = createGlobalStyle`
    div, ol, ul, li,  h1, p, span,a, .icon, label, input{
        background-color:#000000 !important;
        color:#ffffff !important;
    }
    `;

/* -----> Defaulr Export <----- */
export default NightModeStyles;
