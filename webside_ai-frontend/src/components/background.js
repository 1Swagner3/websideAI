import React from "react";
import '../styles/backgroundWrapper.css';
import Logo from "./logo";
function BackgroundWrapper({component}) {
    return (
        <div className="background">
            <Logo/>
            {component}
        </div>
    );
}

export default BackgroundWrapper;