import React from "react";
import '../styles/backgroundWrapper.css';
function BackgroundWrapper({component}) {
    return (
        <div className="background">
            {component}
        </div>
    );
}

export default BackgroundWrapper;