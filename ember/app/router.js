import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('widgets', function() {
    this.route('create');
    this.route('widget', { path: ':widget_id' }, function() {
      this.route('show');
      this.route('edit');
    });
  });
});

export default Router;
