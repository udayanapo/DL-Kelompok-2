import React from "react";
import Header from "../shared/Header";

const PageLayout = (props) => {
    const {children} = props;

    return (
        <>
            <Header />
            {children} 
        </>
    );
};

export default PageLayout;