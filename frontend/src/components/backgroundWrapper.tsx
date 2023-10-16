import React from "react";
import '../styles/backgroundWrapper.css';
import { Logo3D } from "./Logo3d";


type BackgroundWrapperProps = {
  component: React.ReactNode;
};

const BackgroundWrapper: React.FC<BackgroundWrapperProps> = ({ component }) => {
    return (
        <div className="background">

            {component}
        </div>
    );
}

export default BackgroundWrapper;
