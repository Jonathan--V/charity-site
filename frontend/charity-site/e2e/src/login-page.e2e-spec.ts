
import { CommonTest } from './common';
import { LoginPage, USERNAME } from './page-objects/login-page.po';

let specificTests = (getPage: () => LoginPage) => {
  return () => {
    it("Login page", () => {
      getPage().navigateTo()
      getPage().login()
      expect(getPage().getLoggedInText()).toEqual(`You are logged in as ${USERNAME} logout`)
      expect(getPage().logout())
    })
  }
}

CommonTest.commonTest('Login Page', LoginPage, specificTests)
