const dev = {
    url: {
        API: "LOCAL_URL"
    }
};

const staging = {
    url: {
        API: "STAGING_URL"
    }
};

const prod = {
    url: {
        API: "PROD_URL"
    }
};

const get_config = function () {
    switch (process.env.REACT_APP_STAGE) {
        case 'dev':
            return dev;
        case 'staging':
            return staging;
        default:
            return prod;
    }
};

const config = get_config();

export default config;