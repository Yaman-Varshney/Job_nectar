import React from 'react';
import {Box, Grid, Stack, TextField, Typography, Button} from "@mui/material";
import "./styles/SignupPage.css"
const SignupPage = () => {
  return (
    <div className={"signup_page"}>
      <Box className={"signup_box"}>
        <div className={"signup_form"}>
          <Typography className={"signup_form_heading"} variant="h3" component="h3">
            Let's get started
          </Typography>
          <form>
            <Box>
              <Stack spacing={2}>
                <TextField label="Username" variant="outlined" fullWidth={false}/>
                <TextField label="Email" variant="outlined" fullWidth={false} />
                <TextField label="Password" variant="outlined" fullWidth={false} />
                <TextField label="Confirm Password" variant="outlined" fullWidth={false} />
              </Stack>
              <Button variant="contained" className={"signup_btn"}>Sign Up</Button>

            </Box>
          </form>
        </div>
      </Box>
    </div>
  );
};

export default SignupPage;