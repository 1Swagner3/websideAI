import React from "react";
import '../styles/backgroundWrapper.css';
import { Logo3D } from "./Logo3d";
function BackgroundWrapper({component}) {
    return (
        <div className="background">
            <Logo3D/>
            {component}
        </div>
    );
}

export default BackgroundWrapper;