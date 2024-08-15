from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import platform
from jnius import autoclass

if platform == 'android':
    from kivy.clock import Clock

class MyApp(App):
    def build(self):
        btn = Button(text="Open Website", on_press=self.open_website)
        return btn

    def open_website(self, instance):
        if platform == 'android':
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            WebView = autoclass('android.webkit.WebView')
            WebViewClient = autoclass('android.webkit.WebViewClient')
            
            activity = PythonActivity.mActivity
            webview = WebView(activity)
            webview.setWebViewClient(WebViewClient())
            webview.loadUrl("https://www.google.com")
            activity.setContentView(webview)

if __name__ == '__main__':
    MyApp().run()
