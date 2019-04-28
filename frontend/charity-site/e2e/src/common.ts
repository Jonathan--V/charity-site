export class Common {
  static commonTest(page): void {

    it('should be titled correctly', () => {
      expect(page.getTitleText()).toEqual('EVENTS');
    });


  }
}